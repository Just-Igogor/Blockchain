// SPDX-License-Identifier: MIT
// Compatible with OpenZeppelin Contracts ^5.0.0
pragma solidity ^0.8.22;

import {ERC20} from "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract RentalPlatform is ERC20("RentalPlatform", "RNP") {
    struct RentalItem {
        uint256 id; // Уникальный идентификатор предмета
        address owner; // Адрес владельца предмета
        address renter; // Адрес арендатора (если предмет арендуется)
        string name; // Название предмета
        string description; // Описание предмета
        uint256 pricePerDay; // Стоимость аренды в день (в wei)
        uint256 startDate; // Дата начала аренды (если аренда активна)
        uint256 durationDays; // Срок аренды в днях
        bool isAvailable; // Флаг доступности предмета
    }

    struct RentalRecord {
        uint256 itemId; // Идентификатор предмета
        address renter; // Адрес арендатора
        uint256 startDate; // Дата начала аренды
        uint256 durationDays; // Длительность аренды
    }

    address public admin;
    uint256 public nextItemId = 1; // Счётчик для уникальных идентификаторов предметов
    uint256 public nextRentId = 0; // Счётчик для аренд предметов
    mapping(uint256 => RentalItem) public rentalItems; // Хранение данных о предметах
    mapping(address => uint256[]) public rentalForUser; // История аренд для каждого пользователя
    mapping(address => uint256[]) public rentedFromUser; // Какие предметы были арендованы у пользователя
    RentalRecord[] public allRentalRecords; // Общая история аренд

    event ItemListed(uint256 indexed itemId, address indexed owner, string name, string description, uint256 pricePerDay);
    event ItemRented(uint256 indexed itemId, address indexed renter, uint256 startDate, uint256 durationDays, uint256 totalCost);
    event RentalClosed(uint256 indexed itemId, address indexed renter);

    constructor(uint256 initialSupply) {
        admin = msg.sender;
        _mint(msg.sender, initialSupply); // Выпуск токенов для администратора
    }

    // Функция для добавления нового предмета
    function listItem(string memory name, string memory description, uint256 pricePerDay) external {
        require(bytes(name).length > 0, "Name is required");
        require(bytes(description).length > 0, "Description is required");
        require(pricePerDay > 0, "Price must be greater than zero");

        rentalItems[nextItemId] = RentalItem({
            id: nextItemId,
            owner: msg.sender,
            renter: address(0),
            name: name,
            description: description,
            pricePerDay: pricePerDay,
            startDate: 0,
            durationDays: 0,
            isAvailable: true
        });

        emit ItemListed(nextItemId, msg.sender, name, description, pricePerDay);
        nextItemId++;

        closeExpiredRentals(); // Проверяем и завершаем истёкшие аренды
    }

    // Функция для аренды предмета
    function rentItem(uint256 itemId, uint256 durationDays) external payable {
        RentalItem storage item = rentalItems[itemId];
        require(item.isAvailable, "Item is not available for rent");
        require(durationDays > 0, "Duration must be greater than zero");

        uint256 totalCost = durationDays * item.pricePerDay;
        require(msg.value >= totalCost, "Insufficient payment");

        item.isAvailable = false;
        item.renter = msg.sender;
        item.startDate = block.timestamp;
        item.durationDays = durationDays;
        // Трансфер токенов от арендатора владельцу
        _transfer(msg.sender, item.owner, totalCost);
        rentalForUser[msg.sender].push(nextRentId);
        rentedFromUser[item.owner].push(nextRentId);

        allRentalRecords.push(RentalRecord({
            itemId: itemId,
            renter: msg.sender,
            startDate: block.timestamp,
            durationDays: durationDays
        }));

        emit ItemRented(itemId, msg.sender, block.timestamp, durationDays, totalCost);
        nextRentId++;

        closeExpiredRentals(); // Проверяем и завершаем истёкшие аренды
    }

    // Функция для проверки и завершения истёкших аренд
    function closeExpiredRentals() public {
        for (uint256 itemId = 1; itemId < nextItemId; itemId++) {
            RentalItem storage item = rentalItems[itemId];
            if (!item.isAvailable && block.timestamp >= item.startDate + item.durationDays * 1 days) {
                item.isAvailable = true;
                item.renter = address(0);
                item.startDate = 0;
                item.durationDays = 0;
                emit RentalClosed(itemId, item.renter);
            }
        }
    }

    // Функция удаления предмета
    function deleteRental(uint256 itemId) external {
        RentalItem storage item = rentalItems[itemId];
        require(item.isAvailable, "Rental is still active");
        require(msg.sender == item.owner, "Only for owner");

        delete rentalItems[itemId];

        closeExpiredRentals(); // Проверяем и завершаем истёкшие аренды
    }

    // Функция для получения предметов, арендованных у пользователя
    function getRentedFromUser(address user) external view returns (uint256[] memory) {
        return rentedFromUser[user];
    }

    // Функция для получения предметов, арендованных пользователем
    function getRentedForUser(address user) external view returns (uint256[] memory) {
        return rentalForUser[user];
    }

   // Функция для выдачи средств
   function giveTokensToUser(address _to, uint256 _amount) external {
        require(msg.sender == admin, "This action is allowed only for admin");
        require(_amount > 0, "Amount of investing should be more then 0");
        require(balanceOf(admin) >= _amount, "Admin does not hame such amount of tokens");
        _transfer(admin, _to, _amount);
   }
}
