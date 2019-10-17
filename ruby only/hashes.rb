# hashes in ruby are equivalent to dictionaries in python
# they are used to hold key pair values.
# hashes in ruby and python are the same in both only that the mapping sign differs
# i.e ruby => python :
# calling out a key values is still the same in both programming languae


states ={
  "nairobi" => "NRB",
  "Mombasa" => "MSA",
  "Nakuru" => "NAX",
  "MARSABIT" => "MAS"
}
puts states["nairobi"]

# in ruby you can still change the format of the hashe to an even more simple format

states ={
  :nairobi => "NRB",
  :Mombasa => "MSA",
  :Nakuru => "NAX",
  :MARSABIT => "MAS"
}
puts states[:MARSABIT]

# numbers can also be used for hashes
# they are different from list since they give key data values
