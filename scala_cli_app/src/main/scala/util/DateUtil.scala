package util

import java.time.{LocalDate, LocalDateTime}
import java.time.format.{DateTimeFormatter, ResolverStyle}
import java.time.temporal.ChronoUnit.YEARS

object DateUtil {
  private val dateFormatter =
    DateTimeFormatter.ofPattern("uuuu-MM-dd")
      .withResolverStyle(ResolverStyle.STRICT)

  private val dateTimeFormatter =
    DateTimeFormatter.ofPattern("uuuu-MM-dd HH:mm")
      .withResolverStyle(ResolverStyle.STRICT)

  def str2Date(str: String): LocalDate = {
    LocalDate.parse(str, dateFormatter)
  }

  def str2DateTime(str: String): LocalDateTime = {
    LocalDateTime.parse(str, dateTimeFormatter)
  }

  def date2Str(date: LocalDate): String = {
    date.format(dateFormatter)
  }

  def dateTime2Str(date: LocalDateTime): String = {
    date.format(dateTimeFormatter)
  }

  def yearsBetween(localDate1: LocalDate, localDate2: LocalDate): Int = {
    YEARS.between(localDate1, localDate2).toInt
  }

  def compare(localDate1: LocalDate, localDate2: LocalDate): Int = {
    localDate1.compareTo(localDate2).abs
  }
}
