-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema gym_app
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema gym_app
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `gym_app` DEFAULT CHARACTER SET utf8 ;
USE `gym_app` ;

-- -----------------------------------------------------
-- Table `gym_app`.`EXERCISE_TYPE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`EXERCISE_TYPE` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`EXERCISE_TYPE` (
  `exercise_type` NVARCHAR(45) NOT NULL,
  `xfr` INT NULL,
  PRIMARY KEY (`exercise_type`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`USER`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`USER` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`USER` (
  `fname` NVARCHAR(45) NOT NULL,
  `lname` NVARCHAR(45) NOT NULL,
  `dob` DATE NULL,
  `weight` INT NULL,
  `lbs_kg` TINYINT NOT NULL DEFAULT 0,
  `username` NVARCHAR(45) NOT NULL,
  `password` NVARCHAR(256) NOT NULL,
  `salt` NVARCHAR(32) NULL,
  `email` NVARCHAR(45) NULL,
  PRIMARY KEY (`username`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`WORKOUT_PLAN`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`WORKOUT_PLAN` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`WORKOUT_PLAN` (
  `workout_id` INT NOT NULL AUTO_INCREMENT,
  `username` NVARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `start_time` TIME NULL,
  `end_time` TIME NULL,
  `is_started` TINYINT NULL,
  PRIMARY KEY (`workout_id`),
  INDEX `username-fk_idx` (`username` ASC) VISIBLE,
  CONSTRAINT `username-fk`
    FOREIGN KEY (`username`)
    REFERENCES `gym_app`.`USER` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`EXERCISE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`EXERCISE` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`EXERCISE` (
  `workout_id` INT NOT NULL,
  `exercise_type` NVARCHAR(45) NOT NULL,
  `exercise_name` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`exercise_name`, `workout_id`),
  INDEX `exercise-type-fk_idx` (`exercise_type` ASC) VISIBLE,
  CONSTRAINT `workout-id-fk`
    FOREIGN KEY (`workout_id`)
    REFERENCES `gym_app`.`WORKOUT_PLAN` (`workout_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `exercise-type-fk`
    FOREIGN KEY (`exercise_type`)
    REFERENCES `gym_app`.`EXERCISE_TYPE` (`exercise_type`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`MUSCLE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`MUSCLE` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`MUSCLE` (
  `muscle` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`muscle`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`MUSCLE_HIT`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`MUSCLE_HIT` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`MUSCLE_HIT` (
  `muscle` NVARCHAR(45) NOT NULL,
  `activation_level` INT NULL,
  `exercise_type` NVARCHAR(45) NOT NULL,
  PRIMARY KEY (`muscle`, `exercise_type`),
  INDEX `exercise-fk_idx` (`exercise_type` ASC) VISIBLE,
  CONSTRAINT `exercise-fk`
    FOREIGN KEY (`exercise_type`)
    REFERENCES `gym_app`.`EXERCISE_TYPE` (`exercise_type`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `muscle-fk`
    FOREIGN KEY (`muscle`)
    REFERENCES `gym_app`.`MUSCLE` (`muscle`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`EXERCISE_SET`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`EXERCISE_SET` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`EXERCISE_SET` (
  `set_id` INT NOT NULL AUTO_INCREMENT,
  `weight_done` INT NULL,
  `reps_in_reserve` INT NULL,
  `reps` INT NULL,
  `time_taken` INT NULL,
  PRIMARY KEY (`set_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`SETS_DONE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`SETS_DONE` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`SETS_DONE` (
  `exercise` NVARCHAR(45) NOT NULL,
  `set_id` INT NOT NULL,
  `workout_id` INT NOT NULL,
  PRIMARY KEY (`exercise`, `set_id`, `workout_id`),
  INDEX `set-set-id-fk_idx` (`set_id` ASC) VISIBLE,
  INDEX `workout-id-fk-sets_done_idx` (`workout_id` ASC) VISIBLE,
  CONSTRAINT `exersice-set-id-fk`
    FOREIGN KEY (`exercise`)
    REFERENCES `gym_app`.`EXERCISE` (`exercise_name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `set-set-id-fk`
    FOREIGN KEY (`set_id`)
    REFERENCES `gym_app`.`EXERCISE_SET` (`set_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `workout-id-fk-sets_done`
    FOREIGN KEY (`workout_id`)
    REFERENCES `gym_app`.`EXERCISE` (`workout_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`SESSION`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`SESSION` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`SESSION` (
  `username` NVARCHAR(45) NOT NULL,
  `session_id` INT NOT NULL AUTO_INCREMENT,
  `expiration` NVARCHAR(11) NOT NULL,
  PRIMARY KEY (`session_id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE,
  CONSTRAINT `username-session-fk`
    FOREIGN KEY (`username`)
    REFERENCES `gym_app`.`USER` (`username`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
