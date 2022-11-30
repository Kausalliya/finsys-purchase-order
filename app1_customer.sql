-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 29, 2022 at 08:20 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `finsysnew`
--

-- --------------------------------------------------------

--
-- Table structure for table `app1_customer`
--

CREATE TABLE `app1_customer` (
  `customerid` int(11) NOT NULL,
  `title` varchar(10) NOT NULL,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `company` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `gsttype` varchar(100) DEFAULT NULL,
  `gstin` varchar(100) NOT NULL,
  `panno` varchar(100) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `website` varchar(100) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `street` varchar(100) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) NOT NULL,
  `pincode` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `shipstreet` varchar(100) DEFAULT NULL,
  `shipcity` varchar(100) DEFAULT NULL,
  `shipstate` varchar(100) DEFAULT NULL,
  `shippincode` varchar(100) DEFAULT NULL,
  `shipcountry` varchar(100) DEFAULT NULL,
  `opening_balance` double DEFAULT NULL,
  `opening_balance_due` double DEFAULT NULL,
  `date` date DEFAULT NULL,
  `opnbalance_status` varchar(100) NOT NULL,
  `status` varchar(150) NOT NULL,
  `receivables` double DEFAULT NULL,
  `file` varchar(100) NOT NULL,
  `cid_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `app1_customer`
--

INSERT INTO `app1_customer` (`customerid`, `title`, `firstname`, `lastname`, `company`, `location`, `gsttype`, `gstin`, `panno`, `email`, `website`, `mobile`, `street`, `city`, `state`, `pincode`, `country`, `shipstreet`, `shipcity`, `shipstate`, `shippincode`, `shipcountry`, `opening_balance`, `opening_balance_due`, `date`, `opnbalance_status`, `status`, `receivables`, `file`, `cid_id`) VALUES
(1, 'Mr', 'Ram', 'Kumar', 'Rams', 'Kakanadu', 'GST-unregistered', '', 'APPCK7465F', 'saijusunny1301@gmail.com', 'www.finsys.com', '+918281808', 'Thumpunkal (H)', 'tripunithura', 'Kerala', '682312', 'India', 'Thumpunkal (H)', 'tripunithura', 'Kerala', '682312', 'India', NULL, NULL, NULL, 'Default', 'Active', NULL, 'default.jpg', 1),
(2, 'Mr', 'Saiju', 'Sunny', 'Clowns media', 'Kakkanad Ernakulam ', 'GST unregistered', '', 'APPCK7465F', 'saijusunny1301@gmail.com', 'www.finsys.com', '+918281808', 'Thumpunkal (H)', 'tripunithura', 'Kerala', '682312', 'India', 'Thumpunkal (H)', 'tripunithura', 'Kerala', '682312', 'India', NULL, NULL, NULL, 'Default', 'Active', 0, 'default.jpg', 2),
(3, 'Mr', 'Saibu', 'Sunny', 'Clowns media', 'Kakkanad Ernakulam ', 'GST unregistered', '', 'APPCK7465F', 'saijusunny1301@gmail.com', 'www.finsys.com', '+918281808', 'Thumpunkal (H)', 'tripunithura', 'Kerala', '682312', 'India', 'Thumpunkal (H)', 'tripunithura', 'Kerala', '682312', 'India', NULL, NULL, NULL, 'Default', 'Active', 0, 'default.jpg', 2),
(4, 'Mr', 'das', 'adam', 'fdg', 'fgdfgf', 'GST unregistered', '', 'APPCK7465F', 'saijusunny1301@gmail.com', '', '8281808492', 'Thumpunkal (H)', 'tripunithura', 'Kerala', '682312', 'India', 'Thumpunkal (H)', 'tripunithura', 'Kerala', '682312', 'India', 200, 200, '2022-11-22', 'Default', 'Active', NULL, 'default.jpg', 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `app1_customer`
--
ALTER TABLE `app1_customer`
  ADD PRIMARY KEY (`customerid`),
  ADD KEY `app1_customer_cid_id_607bad1d_fk_app1_company_cid` (`cid_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `app1_customer`
--
ALTER TABLE `app1_customer`
  MODIFY `customerid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `app1_customer`
--
ALTER TABLE `app1_customer`
  ADD CONSTRAINT `app1_customer_cid_id_607bad1d_fk_app1_company_cid` FOREIGN KEY (`cid_id`) REFERENCES `app1_company` (`cid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
