-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 01, 2024 at 01:27 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `iot`
--

-- --------------------------------------------------------

--
-- Table structure for table `data`
--

CREATE TABLE `data` (
  `id` int NOT NULL,
  `temperature` double NOT NULL,
  `humidity` double NOT NULL,
  `soilMoisture` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `data`
--

INSERT INTO `data` (`id`, `temperature`, `humidity`, `soilMoisture`) VALUES
(1, 2, 18.4, 99),
(2, 2.4, 20.3, 99),
(3, 1, 21.7, 99),
(4, 1.3, 23, 99),
(5, 1.5, 23.9, 99),
(6, 1.7, 25, 99),
(7, 1.8, 26.1, 99),
(8, 2, 26.2, 99),
(9, 2.1, 26.2, 99),
(10, 2.3, 26.2, 99),
(11, 2.5, 26.2, 99),
(12, 1, 26.2, 99),
(13, 2.5, 26.2, 99),
(14, 2.5, 26.2, 99),
(15, 2.5, 26.2, 99),
(16, 2.4, 26.2, 99),
(17, 2.5, 26.2, 99),
(18, 2.5, 26.2, 99),
(19, 2.5, 26.2, 99),
(20, 2.5, 26.2, 99),
(21, 1, 26.2, 99),
(22, 2.5, 26.2, 99),
(23, 2.5, 26.2, 99),
(24, 1.8, 14.5, 99),
(25, 1.8, 12.8, 99),
(26, 1.8, 11.4, 99),
(27, 1.8, 9.6, 84),
(28, 1.7, 7.7, 84),
(29, 1.7, 6, 81),
(30, 1.8, 5.6, 84),
(31, 1.6, 4.8, 83),
(32, 1.6, 4, 70),
(33, 1.6, 3.2, 67),
(34, 1.5, 27, 72),
(35, 1.5, 26.2, 99),
(36, 1.4, 25.4, 99),
(37, 1.4, 24.6, 99),
(38, 1.4, 23.9, 99),
(39, 1.3, 23.3, 99),
(40, 1.3, 22.8, 99),
(41, 1.3, 22.2, 99),
(42, 1.3, 22, 99),
(43, 1.3, 21.8, 99),
(44, 1.2, 21.4, 99),
(45, 1.2, 20.9, 99),
(46, 1.2, 20.6, 99),
(47, 1.2, 20.4, 99),
(48, 1.2, 20.1, 99),
(49, 1.1, 19.8, 99),
(50, 1.1, 19.6, 99),
(51, 1.1, 19.3, 99),
(52, 1.1, 19.1, 99),
(53, 1.1, 19, 99),
(54, 1, 18.8, 99),
(55, 1, 18.5, 99),
(56, 1, 18.4, 99),
(57, 1, 18.3, 99),
(58, 1, 18.2, 99),
(59, 2.5, 18.1, 99),
(60, 2.5, 18, 99),
(61, 2.5, 17.8, 99),
(62, 2.5, 17.7, 99),
(63, 2.5, 17.6, 99),
(64, 2.5, 17.5, 99),
(65, 2.5, 17.4, 99),
(66, 2.5, 17.3, 99),
(67, 2.4, 17.3, 99),
(68, 2.4, 17.2, 99),
(69, 2.4, 17.2, 99);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int NOT NULL,
  `taikhoan` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `matkhau` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `taikhoan`, `matkhau`) VALUES
(1, 'admin', 'e10adc3949ba59abbe56e057f20f883e');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data`
--
ALTER TABLE `data`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data`
--
ALTER TABLE `data`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
