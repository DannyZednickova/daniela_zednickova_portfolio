-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 25, 2023 at 07:21 AM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `autobazar`
--

-- --------------------------------------------------------

--
-- Table structure for table `cars`
--

CREATE TABLE `cars` (
  `id` int(11) NOT NULL,
  `tip_auto` tinyint(1) DEFAULT NULL,
  `vin` varchar(20) CHARACTER SET utf8 COLLATE utf8_croatian_ci DEFAULT NULL,
  `znacka` varchar(20) CHARACTER SET utf8 COLLATE utf8_czech_ci NOT NULL DEFAULT 'Značka auta',
  `typ` varchar(20) CHARACTER SET utf8 COLLATE utf8_czech_ci NOT NULL,
  `rok` int(11) NOT NULL,
  `motor` varchar(200) CHARACTER SET utf8 COLLATE utf8_czech_ci DEFAULT NULL,
  `barva` text CHARACTER SET utf8 COLLATE utf8_czech_ci,
  `karoserie` text CHARACTER SET utf8 COLLATE utf8_czech_ci,
  `palivo` text CHARACTER SET utf16 COLLATE utf16_czech_ci,
  `kilometry` int(11) DEFAULT NULL,
  `cena` int(11) DEFAULT NULL,
  `vybava` text CHARACTER SET utf8 COLLATE utf8_czech_ci,
  `historie` text CHARACTER SET utf8 COLLATE utf8_czech_ci,
  `serviska` int(1) DEFAULT NULL,
  `dph` int(1) DEFAULT '0',
  `insertdate` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `cars`
--

INSERT INTO `cars` (`id`, `tip_auto`, `vin`, `znacka`, `typ`, `rok`, `motor`, `barva`, `karoserie`, `palivo`, `kilometry`, `cena`, `vybava`, `historie`, `serviska`, `dph`, `insertdate`) VALUES
(19, NULL, 'rwerw', 'BMW', '3 serie', 2020, ' nfgfdf', 'cerna', 'hatchback', 'benzin', 23000, 350000, 'dobra', 'i. majitel', 0, 1, '2021-11-04 09:51:31'),
(20, 0, 'WAUZZZ8T68A026699', 'hovinko', 'fdsfds', 2016, '1,6 TDi', 'modrá', 'hatchback', 'nafta', 35000, 450000, 'klimatizace, tempomat', 'ii. majitel', 0, 0, '2022-30-11 21:29:43');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(10) UNSIGNED NOT NULL,
  `email` varchar(249) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `username` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` tinyint(2) UNSIGNED NOT NULL DEFAULT '0',
  `verified` tinyint(1) UNSIGNED NOT NULL DEFAULT '0',
  `resettable` tinyint(1) UNSIGNED NOT NULL DEFAULT '1',
  `roles_mask` int(10) UNSIGNED NOT NULL DEFAULT '0',
  `registered` int(10) UNSIGNED NOT NULL,
  `last_login` int(10) UNSIGNED DEFAULT NULL,
  `force_logout` mediumint(7) UNSIGNED NOT NULL DEFAULT '0'
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `username`, `status`, `verified`, `resettable`, `roles_mask`, `registered`, `last_login`, `force_logout`) VALUES
(3, 'd@gmail.com', '$2y$10$9g71Js4Khh4r/.oUlDv0Ye0RXzTZHRclrE2XWqRltlpsHkj3mZk.K', 'dde', 0, 0, 1, 0, 1610004377, NULL, 0),
(2, 'danny.drabkova@gmail.com', '$2y$10$TOg1AHMFRP.WX8TgO2Fkp.p4.6BQCgvy4Ss5IgJHLQF3/uOlNsnBm', 'DANIELAZED', 1, 1, 1, 0, 1609963290, 1669843709, 0),
(4, 'pavel@gmail.com', '$2y$10$m8oeOMRo6bgIkdSdvTVR6ehlRY1qU.l0T.53WsHmNpuZwSFTBMrh.', 'pavel', 0, 0, 1, 0, 1631863371, NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `users_confirmations`
--

CREATE TABLE `users_confirmations` (
  `id` int(10) UNSIGNED NOT NULL,
  `user_id` int(10) UNSIGNED NOT NULL,
  `email` varchar(249) COLLATE utf8mb4_unicode_ci NOT NULL,
  `selector` varchar(16) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `token` varchar(255) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `expires` int(10) UNSIGNED NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users_confirmations`
--

INSERT INTO `users_confirmations` (`id`, `user_id`, `email`, `selector`, `token`, `expires`) VALUES
(1, 1, 'danny.drabkova@gmail.com', '5daD-SuopUQ_K7OF', '$2y$10$He2px1LFadNYVW8sVKeNnOtQeUaGs3Tbsi.F4Vt4iHWZm2X3dVJVK', 1610048656),
(2, 2, 'danny.drabkova@gmail.com', 'YcWWS4ho_wiNuF2X', '$2y$10$q/oSoEZhQojXJw8P7ITrduRjNY6c.fUOSCJnWO30nsEhXqF0srrQG', 1610049690),
(3, 3, 'd@gmail.com', 'Orb_UL5Mjw5xAeb8', '$2y$10$0xQphKtqd7GvFow640diCOBNMUwpt0XUbDtKeOR..wF9o0d5ABa2K', 1610090777),
(4, 4, 'pavel@gmail.com', 'b9Nwpr2DyPgL3G0g', '$2y$10$FbdPZLiG/TdjngaBnYgSoePtXk0sO.BerdZA7ZB./z2qHN7lrGThe', 1631949772);

-- --------------------------------------------------------

--
-- Table structure for table `users_remembered`
--

CREATE TABLE `users_remembered` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user` int(10) UNSIGNED NOT NULL,
  `selector` varchar(24) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `token` varchar(255) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `expires` int(10) UNSIGNED NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_resets`
--

CREATE TABLE `users_resets` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `user` int(10) UNSIGNED NOT NULL,
  `selector` varchar(20) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `token` varchar(255) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `expires` int(10) UNSIGNED NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_throttling`
--

CREATE TABLE `users_throttling` (
  `bucket` varchar(44) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `tokens` float UNSIGNED NOT NULL,
  `replenished_at` int(10) UNSIGNED NOT NULL,
  `expires_at` int(10) UNSIGNED NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `users_throttling`
--

INSERT INTO `users_throttling` (`bucket`, `tokens`, `replenished_at`, `expires_at`) VALUES
('QduM75nGblH2CDKFyk0QeukPOwuEVDAUFE54ITnHM38', 72.05, 1669843709, 1670383709),
('PZ3qJtO_NLbJfRIP-8b4ME4WA3xxc6n9nbCORSffyQ0', 4, 1631863372, 1632295372),
('OMhkmdh1HUEdNPRi-Pe4279tbL5SQ-WMYf551VVvH8U', 18.0144, 1669843542, 1669879542),
('iP0ihsbQpN0hiamD86a7eIGoYP3nwWAYY775sHMMEns', 498.075, 1669843542, 1670016342);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cars`
--
ALTER TABLE `cars`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `users_confirmations`
--
ALTER TABLE `users_confirmations`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `selector` (`selector`),
  ADD KEY `email_expires` (`email`,`expires`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users_remembered`
--
ALTER TABLE `users_remembered`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `selector` (`selector`),
  ADD KEY `user` (`user`);

--
-- Indexes for table `users_resets`
--
ALTER TABLE `users_resets`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `selector` (`selector`),
  ADD KEY `user_expires` (`user`,`expires`);

--
-- Indexes for table `users_throttling`
--
ALTER TABLE `users_throttling`
  ADD PRIMARY KEY (`bucket`),
  ADD KEY `expires_at` (`expires_at`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cars`
--
ALTER TABLE `cars`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users_confirmations`
--
ALTER TABLE `users_confirmations`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users_remembered`
--
ALTER TABLE `users_remembered`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_resets`
--
ALTER TABLE `users_resets`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
