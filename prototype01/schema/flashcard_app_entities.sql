SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `flashcard_app` DEFAULT CHARACTER SET utf8 ;
USE `flashcard_app` ;

-- -----------------------------------------------------
-- Table `flashcard_app`.`flashcard_decks`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `flashcard_app`.`flashcard_decks` ;

CREATE TABLE IF NOT EXISTS `flashcard_app`.`flashcard_decks` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_active` BINARY(1) NULL DEFAULT '1',
  `created_by` INT(11) NULL DEFAULT NULL,
  `title` VARCHAR(127) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `title_UNIQUE` (`title` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `flashcard_app`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `flashcard_app`.`users` ;

CREATE TABLE IF NOT EXISTS `flashcard_app`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_active` BINARY(1) NULL DEFAULT '1',
  `first_name` VARCHAR(45) NULL DEFAULT NULL,
  `last_name` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `flashcard_app`.`flashcards`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `flashcard_app`.`flashcards` ;

CREATE TABLE IF NOT EXISTS `flashcard_app`.`flashcards` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_active` BINARY(1) NULL DEFAULT '1',
  `question_text` VARCHAR(256) NULL DEFAULT NULL,
  `answer_text` VARCHAR(127) NULL DEFAULT NULL,
  `created_by` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `flashcard_app`.`flashcard_responses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `flashcard_app`.`flashcard_responses` ;

CREATE TABLE IF NOT EXISTS `flashcard_app`.`flashcard_responses` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_active` BINARY(1) NULL DEFAULT '1',
  `response` VARCHAR(127) NULL DEFAULT NULL,
  `flashcard_id` INT(11) NULL DEFAULT NULL,
  `user_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `card_id_fk_idx` (`flashcard_id` ASC),
  INDEX `user_id_fk_idx` (`user_id` ASC),
  CONSTRAINT `user_id_fk`
    FOREIGN KEY (`user_id`)
    REFERENCES `flashcard_app`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `card_id_fk`
    FOREIGN KEY (`flashcard_id`)
    REFERENCES `flashcard_app`.`flashcards` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `flashcard_app`.`tags`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `flashcard_app`.`tags` ;

CREATE TABLE IF NOT EXISTS `flashcard_app`.`tags` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_active` BINARY(1) NULL DEFAULT '1',
  `text` VARCHAR(127) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `text_UNIQUE` (`text` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `flashcard_app`.`flashcard_decks_has_flashcards`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `flashcard_app`.`flashcard_decks_has_flashcards` ;

CREATE TABLE IF NOT EXISTS `flashcard_app`.`flashcard_decks_has_flashcards` (
  `flashcard_decks_id` INT(11) NOT NULL,
  `flashcards_id` INT(11) NOT NULL,
  PRIMARY KEY (`flashcard_decks_id`, `flashcards_id`),
  INDEX `fk_flashcard_decks_has_flashcards_flashcards1_idx` (`flashcards_id` ASC),
  INDEX `fk_flashcard_decks_has_flashcards_flashcard_decks1_idx` (`flashcard_decks_id` ASC),
  CONSTRAINT `fk_flashcard_decks_has_flashcards_flashcard_decks1`
    FOREIGN KEY (`flashcard_decks_id`)
    REFERENCES `flashcard_app`.`flashcard_decks` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_flashcard_decks_has_flashcards_flashcards1`
    FOREIGN KEY (`flashcards_id`)
    REFERENCES `flashcard_app`.`flashcards` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
