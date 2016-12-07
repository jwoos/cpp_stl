#counts the number of specific words in a text

puts "Please input some text"
text = gets.chomp

words = text.split(" ")

frequencies = Hash.new(0)

words.each {|word| frequencies[word] += 1}
frequencies = frequencies.sort_by {|word, count| count}
#frequencies.reverse

frequencies.reverse.each {|word, count| puts word + " " + count.to_s}