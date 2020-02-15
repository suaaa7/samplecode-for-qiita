package app

import util.DateUtil
import scala.annotation.tailrec
import scala.io.StdIn.readLine
import scala.util.{Success, Try}

object CLIApp extends App {
  val date1 = DateUtil.str2Date(getInput)
  val date2 = DateUtil.str2Date(getInput)
  println(s"date1: ${DateUtil.date2Str(date1)}")
  println(s"date2: ${DateUtil.date2Str(date2)}")
  println(s"yearsBetween: ${DateUtil.yearsBetween(date1, date2)}")
  println(s"compare     : ${DateUtil.compare(date1, date2)}")

  @tailrec
  def getInput: String = {
    println("入力してください (例: 2020-01-01)")
    val input = readLine()

    Try(DateUtil.str2Date(input)) match {
      case Success(_) => input
      case _          => getInput
    }
  }
}
