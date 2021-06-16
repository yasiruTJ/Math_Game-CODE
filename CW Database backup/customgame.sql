-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2020 at 12:04 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `customgame`
--

-- --------------------------------------------------------

--
-- Table structure for table `easy_mode`
--

CREATE TABLE `easy_mode` (
  `Name` varchar(8) DEFAULT NULL,
  `Total_Questions` varchar(3) DEFAULT NULL,
  `Correct_Answers` varchar(3) DEFAULT NULL,
  `Score` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `easy_mode`
--

INSERT INTO `easy_mode` (`Name`, `Total_Questions`, `Correct_Answers`, `Score`) VALUES
('Yasiru', '6', '6', '100'),
('Kushan', '8', '8', '100'),
('Kumar', '8', '0', '0.0');

-- --------------------------------------------------------

--
-- Table structure for table `hard_mode`
--

CREATE TABLE `hard_mode` (
  `Name` varchar(8) DEFAULT NULL,
  `Total_Questions` varchar(3) DEFAULT NULL,
  `Correct_Answers` varchar(3) DEFAULT NULL,
  `Score` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hard_mode`
--

INSERT INTO `hard_mode` (`Name`, `Total_Questions`, `Correct_Answers`, `Score`) VALUES
('ui', '5', '2', '40.');

-- --------------------------------------------------------

--
-- Table structure for table `medium_mode`
--

CREATE TABLE `medium_mode` (
  `Name` varchar(8) DEFAULT NULL,
  `Total_Questions` varchar(3) DEFAULT NULL,
  `Correct_Answers` varchar(3) DEFAULT NULL,
  `Score` varchar(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `medium_mode`
--

INSERT INTO `medium_mode` (`Name`, `Total_Questions`, `Correct_Answers`, `Score`) VALUES
('h', '4', '1', '25.');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
