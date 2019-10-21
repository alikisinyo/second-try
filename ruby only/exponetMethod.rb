 def power(base , powerNum)
   result = 1
   powerNum.times do |index|
     result = result * base
   end
   return result
 end


 puts power(2,3)
