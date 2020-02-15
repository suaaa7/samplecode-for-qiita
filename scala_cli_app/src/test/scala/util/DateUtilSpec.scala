package util

import java.time.{LocalDate, LocalDateTime}
import org.scalatest.{FunSpec, Matchers}

class DateUtilSpec extends FunSpec with Matchers{
  describe("str2Date") {
    it("String => LocalDate") {
      val expected = LocalDate.of(2020, 1, 1)
      DateUtil.str2Date("2020-01-01") shouldEqual expected
    }
  }

  describe("str2DateTime") {
    it("String => LocalDateTime") {
      val expected = LocalDateTime.of(2020, 1, 1, 0, 30, 0)
      DateUtil.str2DateTime("2020-01-01 00:30") shouldEqual expected
    }
  }

  describe("date2Str") {
    it("LocalDate => String") {
      val input = LocalDate.of(2020, 1, 1)
      DateUtil.date2Str(input) shouldEqual "2020-01-01"
    }
  }

  describe("dateTime2Str") {
    it("LocalDate => String") {
      val input = LocalDateTime.of(2020, 1, 1, 0, 30, 0)
      DateUtil.dateTime2Str(input) shouldEqual "2020-01-01 00:30"
    }
  }

  describe("yearsBetween") {
    it("calculate age") {
      val input1 = LocalDate.of(2018, 4, 1)
      val input2 = LocalDate.of(2020, 1, 1)
      DateUtil.yearsBetween(input1, input2) shouldEqual 1
    }
  }

  describe("compare") {
    it("calculate age") {
      val input1 = LocalDate.of(2018, 4, 1)
      val input2 = LocalDate.of(2020, 1, 1)
      DateUtil.compare(input1, input2) shouldEqual 2
    }
  }
}
