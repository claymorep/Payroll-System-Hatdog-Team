-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 18, 2024 at 11:29 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hatdogdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_pass`
--

CREATE TABLE `admin_pass` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_pass`
--

INSERT INTO `admin_pass` (`username`, `password`) VALUES
('admin', 'password'),
('admin2', 'password'),
('admin3', 'password');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `job_id` varchar(255) NOT NULL,
  `job_dept` varchar(255) NOT NULL,
  `job_name` varchar(255) NOT NULL,
  `job_desc` text NOT NULL,
  `salary_range` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`job_id`, `job_dept`, `job_name`, `job_desc`, `salary_range`) VALUES
('301', 'IT Department', 'Database Developer', 'A person who works on the database.', '70000'),
('302', 'IT Department', 'Database Developer', 'A person who works on the database.', '65000'),
('303', 'Engineering Department', 'Lab Technician', 'A person who works on the lab materials.', '90000');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `em_id` varchar(255) NOT NULL,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  `age` varchar(255) NOT NULL,
  `birthdate` date NOT NULL,
  `gender` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `contact_num` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `image` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`em_id`, `firstname`, `lastname`, `age`, `birthdate`, `gender`, `address`, `contact_num`, `email`, `status`, `image`) VALUES
('101', 'Carl', 'Naval', '22', '2002-02-01', 'Male', '6 Burgos St, Concepcion, Malabon City', '09954890323', 'carlnaval123.cpe@gmail.com', 'Full Time', 'image1.jpg'),
('102', 'adasd', 'asdf', '21', '2003-03-15', 'Female', 'Quezon City', '09953232323', 'theresa@gmail.com', 'Full Time', 'image2.jpg'),
('103', 'Claymore', 'Paguinto', '21', '2002-08-12', 'Male', 'Cavite', '094328490238', 'claymore@gmail.com', 'Full Time', NULL),
('104', 'Annyeonghaseyo', 'My ', '31', '2002-08-12', 'Male', 'Manila', '0980942340', 'manila@gmail.com`', 'Full Time', NULL),
('108', 'asdas', 'asdasd', '21', '2002-09-12', 'Male', 'Luzon Expressway', 'adas', 'asdas', 'asdas', NULL),
('109', 'asdsdfg', 'io', 'uh', '0000-00-00', 'uioh', 'iouh', 'io0h', 'iohj', 'iophoi', NULL),
('111', 'asdhoiashdio', 'ioh', 'ioh', '0000-00-00', 'ghhj', 'ohb', 'uih', 'iogb', 'uiopgbui9', NULL),
('112', '', '', '', '0000-00-00', '', '', '', '', '', NULL),
('124', 'edfdfgfdfg', 'iohfdgdfgg', 'oi', '0000-00-00', 'hbiohbiohbnyhuigh', 'igiogloug', 'olyuguiplgolpugpl', 'guigoluiguiol', 'guiogluoghl', NULL),
('125', 'Gab', 'Lopez', '21', '2002-12-21', 'Male', 'Manila Quezon', '084092384', 'jsdfjsd', 'Full Time', NULL),
('adasd', 'asdasd', 'asdasd', 'adasda', '0000-00-00', 'sdasd', 'asdasd', 'asdg', 'dfgdfb', 'gdfg', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `payroll`
--

CREATE TABLE `payroll` (
  `em_id` varchar(255) NOT NULL,
  `job_id` varchar(255) NOT NULL,
  `salary_id` varchar(255) NOT NULL,
  `date` datetime NOT NULL,
  `report` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payroll`
--

INSERT INTO `payroll` (`em_id`, `job_id`, `salary_id`, `date`, `report`) VALUES
('101', '301', '401', '2024-03-06 09:49:52', 'This is a report on the person, woo!'),
('125', '302', '402', '2024-03-18 16:53:50', 'report1'),
('adasd', '301', '401', '2024-03-18 16:55:42', 'report1'),
('102', '301', '401', '2024-03-18 18:28:11', 'report1');

-- --------------------------------------------------------

--
-- Table structure for table `salary`
--

CREATE TABLE `salary` (
  `salary_id` varchar(255) NOT NULL,
  `job_id` varchar(255) NOT NULL,
  `monthly_salary` int(11) NOT NULL,
  `annual_salary` int(11) NOT NULL,
  `bonus` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `salary`
--

INSERT INTO `salary` (`salary_id`, `job_id`, `monthly_salary`, `annual_salary`, `bonus`) VALUES
('401', '301', 35000, 420000, 50000),
('402', '302', 75000, 2147483647, 10000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`job_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`em_id`);

--
-- Indexes for table `payroll`
--
ALTER TABLE `payroll`
  ADD KEY `em_id` (`em_id`),
  ADD KEY `job_id` (`job_id`),
  ADD KEY `salary_id` (`salary_id`);

--
-- Indexes for table `salary`
--
ALTER TABLE `salary`
  ADD PRIMARY KEY (`salary_id`),
  ADD KEY `salary_ibfk_1` (`job_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `payroll`
--
ALTER TABLE `payroll`
  ADD CONSTRAINT `payroll_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `department` (`job_id`),
  ADD CONSTRAINT `payroll_ibfk_2` FOREIGN KEY (`em_id`) REFERENCES `employee` (`em_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `payroll_ibfk_3` FOREIGN KEY (`salary_id`) REFERENCES `salary` (`salary_id`);

--
-- Constraints for table `salary`
--
ALTER TABLE `salary`
  ADD CONSTRAINT `salary_ibfk_1` FOREIGN KEY (`job_id`) REFERENCES `department` (`job_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
