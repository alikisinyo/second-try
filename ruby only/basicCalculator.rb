# making a calculator
puts "Enter a number: "
num1 = gets.chomp()
puts "Enter another number: "
num2 = gets.chomp()
# after debbugin code kindly run it again then try on the terminal
# adding two variables on a string only concatinates them but does no convert to a specific number
# to deal with this issue (to_i) but incases of floating numers being introduced the results may be wrong
# puts (num1.to_i + num2.to_i)
# to solve this we use (to_f) this fixes all the issues for both floating and intergers
# dont forget to run again
puts (num1.to_f + num2.to_f)
# these set of codes will give you the same results as in the puts above
# num1 = gets.chomp().to_f
# num1 = gets.chomp().to_f
# puts (num1 + num2)
