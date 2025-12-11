-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-12-2025 a las 16:47:23
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_estacionamiento`
--
CREATE DATABASE IF NOT EXISTS `bd_estacionamiento` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `bd_estacionamiento`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registros`
--

CREATE TABLE `registros` (
  `id` int(11) NOT NULL,
  `tipo_evento` varchar(20) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `placa_detectada` varchar(20) DEFAULT NULL,
  `imagen_evidencia` longblob DEFAULT NULL,
  `id_vehiculo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registros`
--

INSERT INTO `registros` (`id`, `tipo_evento`, `fecha`, `hora`, `placa_detectada`, `imagen_evidencia`, `id_vehiculo`) VALUES
(1, 'Entrada', '2025-12-11', '07:45:00', 'ABC-101', NULL, 1),
(2, 'Entrada', '2025-12-11', '08:00:15', 'XYZ-202', NULL, 2),
(3, 'Denegado', '2025-12-11', '09:15:00', 'BAN-000', NULL, 5),
(4, 'Salida', '2025-12-11', '13:30:00', 'ABC-101', NULL, 1),
(5, 'Entrada', '2025-12-11', '07:30:00', 'JFK-303', NULL, 3),
(6, 'Denegado', '2025-12-11', '12:00:00', 'UNK-999', NULL, NULL),
(7, 'Entrada', '2025-12-11', '10:05:00', 'LMN-404', NULL, 4),
(8, 'Salida', '2025-12-11', '15:00:00', 'XYZ-202', NULL, 2),
(9, 'Entrada', '2025-12-10', '14:20:00', 'WDR-888', NULL, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido_paterno` varchar(100) NOT NULL,
  `apellido_materno` varchar(100) NOT NULL,
  `rol` varchar(50) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `estado` tinyint(1) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellido_paterno`, `apellido_materno`, `rol`, `email`, `password`, `estado`) VALUES
(1, 'Super', 'Admin', 'Sistema', 'Sudote', 'sudote@vera.security', '240be518fabd2724ddb6f04eeb1da5967448d7e831c08c8fa822809f74c720a9', 1),
(2, 'Ana', 'Torres', 'Gil', 'Estudiante', NULL, NULL, 1),
(3, 'Carlos', 'Ruiz', 'Mendez', 'Docente', NULL, NULL, 1),
(4, 'Sofia', 'López', 'Rio', 'Administrativo', NULL, NULL, 1),
(5, 'Miguel', 'Angel', 'Soto', 'Trabajador', NULL, NULL, 1),
(6, 'Lucia', 'Fernandez', 'Paz', 'Estudiante', NULL, NULL, 0),
(7, 'Roberto', 'Gomez', 'Bolaños', 'Docente', NULL, NULL, 1),
(8, 'Diana', 'Prince', 'Themyscira', 'Estudiante', NULL, NULL, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `vehiculos`
--

CREATE TABLE `vehiculos` (
  `id` int(11) NOT NULL,
  `marca` varchar(50) DEFAULT NULL,
  `modelo` varchar(50) DEFAULT NULL,
  `color` varchar(30) DEFAULT NULL,
  `placa` varchar(20) NOT NULL,
  `anio` int(11) DEFAULT NULL,
  `id_usuario` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `vehiculos`
--

INSERT INTO `vehiculos` (`id`, `marca`, `modelo`, `color`, `placa`, `anio`, `id_usuario`) VALUES
(1, 'Nissan', 'Versa', 'Rojo', 'ABC-101', 2020, 2),
(2, 'Toyota', 'Corolla', 'Blanco', 'XYZ-202', 2019, 3),
(3, 'Honda', 'Civic', 'Gris', 'JFK-303', 2022, 4),
(4, 'Ford', 'Fiesta', 'Azul', 'LMN-404', 2015, 5),
(5, 'Chevrolet', 'Aveo', 'Negro', 'BAN-000', 2018, 6),
(6, 'Volkswagen', 'Jetta', 'Plata', 'JET-555', 2021, 7),
(7, 'Jeep', 'Renegade', 'Naranja', 'WDR-888', 2023, 8),
(8, 'Volkswagen', 'Tiguan', 'Azul', 'FYT156D', 2025, 5);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `registros`
--
ALTER TABLE `registros`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_vehiculo` (`id_vehiculo`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `placa` (`placa`),
  ADD KEY `id_usuario` (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `registros`
--
ALTER TABLE `registros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `registros`
--
ALTER TABLE `registros`
  ADD CONSTRAINT `registros_ibfk_1` FOREIGN KEY (`id_vehiculo`) REFERENCES `vehiculos` (`id`) ON DELETE SET NULL;

--
-- Filtros para la tabla `vehiculos`
--
ALTER TABLE `vehiculos`
  ADD CONSTRAINT `vehiculos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
