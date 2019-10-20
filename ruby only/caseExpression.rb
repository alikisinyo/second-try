# used to check a bunch of different data
# def getDayname(day)
#   day_name = ""
#
#   case day
#   when "mon"
#     day_name = "Monday"
#   when "tue"
#     day_name = "tuesday"
#   when "wed"
#     day_name = "wednesday"
#   when "thur"
#     day_name = "thursday"
#   when "fri"
#     day_name = "friday"
#   when "sat"
#     day_name = "satarday"
#   when "sun"
#     day_name = "sunday"
#   else
#     day_name = "invalid day name"
#
#   end
#   return day_name
# end
#
# puts getDayname("mon")

def monthsYear(month)
  month_name = ""

  case month
  when "jan"
    month_name = "January"
  when "feb"
    month_name = "february"
  when "march"
    month_name = "march"
  when "apr"
    month_name = "april"
  when "may"
    month_name = "may"
  when "jun"
    month_name = "june"
  when "july"
    month_name = "july"
  when "aug"
    month_name = "august"
  when "sep"
    month_name = "september"
  when "oct"
    month_name = "october"
  when "nov"
    month_name = "November"
  when "dec"
    month_name = "December"
  else
    puts "invalid month name"
  end
end

puts monthsYear("feb")
