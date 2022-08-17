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
  `exercise_type_name` NVARCHAR(45) NOT NULL,
  `exercise_type_id` INT NOT NULL AUTO_INCREMENT,
  `xfr` INT NULL,
  PRIMARY KEY (`exercise_type_id`))
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
  `user_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`user_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`WORKOUT_PLAN`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`WORKOUT_PLAN` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`WORKOUT_PLAN` (
  `workout_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `date` DATE NOT NULL,
  `start_time` TIME NULL,
  `end_time` TIME NULL,
  `is_started` TINYINT NULL,
  PRIMARY KEY (`workout_id`),
  INDEX `users-workout_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `user-work-fk`
    FOREIGN KEY (`user_id`)
    REFERENCES `gym_app`.`USER` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`EXERCISE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`EXERCISE` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`EXERCISE` (
  `workout_id` INT NOT NULL,
  `exersice_type` INT NOT NULL,
  `exersice_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`exersice_id`),
  INDEX `exercise-id-fk_idx` (`exersice_type` ASC) VISIBLE,
  CONSTRAINT `workout-id-fk`
    FOREIGN KEY (`workout_id`)
    REFERENCES `gym_app`.`WORKOUT_PLAN` (`workout_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `exercise-type-id-fk`
    FOREIGN KEY (`exersice_type`)
    REFERENCES `gym_app`.`EXERCISE_TYPE` (`exercise_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`MUSCLE`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`MUSCLE` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`MUSCLE` (
  `muscle` NVARCHAR(45) NOT NULL,
  `muscle_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`muscle_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`MUSCLE_HIT`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`MUSCLE_HIT` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`MUSCLE_HIT` (
  `exersice_type_id` INT NOT NULL,
  `muscle_id` INT NOT NULL,
  `activation_level` INT NULL,
  PRIMARY KEY (`exersice_type_id`, `muscle_id`),
  INDEX `muscle-id-fk_idx` (`muscle_id` ASC) VISIBLE,
  CONSTRAINT `exercise-type-id-fk`
    FOREIGN KEY (`exersice_type_id`)
    REFERENCES `gym_app`.`EXERCISE_TYPE` (`exercise_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `muscle-id-fk`
    FOREIGN KEY (`muscle_id`)
    REFERENCES `gym_app`.`MUSCLE` (`muscle_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gym_app`.`SET`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gym_app`.`SET` ;

CREATE TABLE IF NOT EXISTS `gym_app`.`SET` (
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
  `exercise_id` INT NOT NULL,
  `set_id` INT NOT NULL,
  PRIMARY KEY (`exercise_id`, `set_id`),
  INDEX `set-set-id-fk_idx` (`set_id` ASC) VISIBLE,
  CONSTRAINT `exersice-set-id-fk`
    FOREIGN KEY (`exercise_id`)
    REFERENCES `gym_app`.`EXERCISE` (`exersice_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `set-set-id-fk`
    FOREIGN KEY (`set_id`)
    REFERENCES `gym_app`.`SET` (`set_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
