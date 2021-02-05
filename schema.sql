-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         5.7.24 - MySQL Community Server (GPL)
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para edistribucion
CREATE DATABASE IF NOT EXISTS `edistribucion` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `edistribucion`;

-- Volcando estructura para tabla edistribucion.consumos
CREATE TABLE IF NOT EXISTS `consumos` (
  `cups` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `hour` varchar(100) NOT NULL,
  `invoiced` int(1) DEFAULT NULL,
  `obtainingMethod` varchar(100) DEFAULT NULL,
  `real` int(1) DEFAULT NULL,
  `value` decimal(6,3) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`cups`,`date`,`hour`),
  CONSTRAINT `FK_consumos_cups` FOREIGN KEY (`cups`) REFERENCES `cups` (`cups`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla edistribucion.cups
CREATE TABLE IF NOT EXISTS `cups` (
  `cups` varchar(100) NOT NULL,
  `titular` varchar(100) DEFAULT NULL,
  `direccion` varchar(100) DEFAULT NULL,
  `id` varchar(100) DEFAULT NULL,
  `asr` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`cups`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla edistribucion.login
CREATE TABLE IF NOT EXISTS `login` (
  `user` varchar(50) NOT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`user`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- La exportación de datos fue deseleccionada.

-- Volcando estructura para tabla edistribucion.tramos
CREATE TABLE IF NOT EXISTS `tramos` (
  `tipo` varchar(2) DEFAULT NULL,
  `hora` varchar(100) NOT NULL,
  PRIMARY KEY (`hora`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla edistribucion.tramos: 24 rows
/*!40000 ALTER TABLE `tramos` DISABLE KEYS */;
INSERT INTO `tramos` (`tipo`, `hora`) VALUES
	('P2', '01 - 02 h'),
	('P2', '02 - 03 h'),
	('P2', '03 - 04 h'),
	('P2', '04 - 05 h'),
	('P2', '05 - 06 h'),
	('P2', '06 - 07 h'),
	('P2', '07 - 08 h'),
	('P2', '08 - 09 h'),
	('P2', '09 - 10 h'),
	('P2', '10 - 11 h'),
	('P2', '11 - 12 h'),
	('P1', '12 - 13 h'),
	('P1', '13 - 14 h'),
	('P1', '14 - 15 h'),
	('P1', '15 - 16 h'),
	('P1', '16 - 17 h'),
	('P1', '17 - 18 h'),
	('P1', '18 - 19 h'),
	('P1', '19 - 20 h'),
	('P1', '20 - 21 h'),
	('P1', '21 - 22 h'),
	('P2', '22 - 23 h'),
	('P2', '00 - 01 h'),
	('P2', '23 - 00 h');

-- La exportación de datos fue deseleccionada.

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
