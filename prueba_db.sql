-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 27, 2026 at 02:07 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `prueba_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `trabajo`
--

CREATE TABLE `trabajo` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) DEFAULT NULL,
  `tipo_trabajo` varchar(50) DEFAULT NULL,
  `autor` varchar(100) DEFAULT NULL,
  `universidad` varchar(100) DEFAULT NULL,
  `palabras_claves` text DEFAULT NULL,
  `resumen` text DEFAULT NULL,
  `curso` varchar(50) DEFAULT NULL,
  `imagen` longblob DEFAULT NULL,
  `pdf` varchar(255) DEFAULT NULL,
  `ciudad` varchar(100) DEFAULT NULL,
  `especialidad` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `trabajo`
--
ALTER TABLE `trabajo`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `trabajo`
--
ALTER TABLE `trabajo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
