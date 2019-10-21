# class Book
#   attr_accessor :title, :author, :pages
#
# end
#
#
# book1 = Book.new()
# book1.title = "ALI"
# book1.author = "ALI Kisinyo"
# book1.pages = 500
#
# puts book1.pages
#
# book2 = Book.new()
# book2.title = "skylar"
# book2.author = "skylar Kisinyo"
# book2.pages = 500
#
# puts book2.author

class Unit
  attr_accessor :name, :capacity, :motto, :location

end

unit1 = Unit.new()
unit1.name = "Moi Airbase"
unit1.capacity = 1000
unit1.motto = "Imara Angani"
unit1.location = "Eastleigh"

unit2 = Unit.new()
unit2.name = "DEFTEC"
unit2.capacity = 1000
unit2.motto = "non"
unit2.location = "Embakasi"

unit3 = Unit.new()
unit3.name = "7 Kenya Rifles"
unit3.capacity = 1000
unit3.motto = "Maroon Commandos"
unit3.location = "Langata"

puts unit3.location
