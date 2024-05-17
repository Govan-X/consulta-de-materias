CREATE TABLE `asignaturas` (
  `idAsignaturas` INT NOT NULL AUTO_INCREMENT,
  `claveAsignatura` INT NOT NULL,
  `nombreAsignatura` VARCHAR(60) NOT NULL,
  `grupo` INT NOT NULL,
  `profesor` VARCHAR(50) NOT NULL,
  `salon` VARCHAR(15) NOT NULL,
  `dia` VARCHAR(15) NOT NULL,
  `hora` VARCHAR(20) NOT NULL,
  `lugaresDisponibles` INT(2) NOT NULL,
  PRIMARY KEY (`idAsignaturas`),
  UNIQUE INDEX `claveAsignatura_UNIQUE` (`claveAsignatura` ASC) VISIBLE,
  UNIQUE INDEX `idAsignaturas_UNIQUE` (`idAsignaturas` ASC) VISIBLE);