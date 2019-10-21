# a stands for appending
# r stands for read only
# File.open("python.txt", "a") do |file|
#   file.write("\nlearning writing in ruby")
#
# end
# the next method overwrites everything completely.

# File.open("python.txt", "w") do |file|
#    file.write("string")
#
# end
# creating files
File.open("index.html", "w") do |file|
  file.write("<h1> hello Ali</h1>")

end
