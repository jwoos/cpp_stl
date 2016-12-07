#print using puts
puts "the calculator is ready for use!"
puts "please input a number"

#variable number1 is equal to user input (gets)
# .to_i method is called to transform it into an integer
#.to_f method is called to transform it into a floating point number
number1 = gets.to_f

#for the future to verify that input is an integer and if not give a chance to run again
if number1.is_a? integer = false
	puts "please put in a number"
 	puts "your first number was #{number1}"
 	puts "please input a second number"
	number2 = gets.to_f
	puts "your second number was #{number2}"
else
 	puts "Your first number was #{number1}"
 	number1.to_f
end

puts "what do you want to do? (add, subtract, multiply, divide)"
puts "you can do more! (divide_remainder, exponent)"
#.chomp method removes /n (new line character)
operation = gets.chomp

#four function
if operation == "add"
	answer = number1 + number2
	puts "your answwer is #{answer}"
elsif operation == "subtract"
	answer = number1 - number2
	puts "your answwer is #{answer}"
elsif operation == "multiply"
	answer = number1 * number2
	puts "your answwer is #{answer}"
elsif operation == "divide"
	answer = number1 / number2
	puts "your answwer is #{answer}"
elsif operation == "divide_remainder"
	answer = number1 / number2
	remainder = number1 % number2
	puts "your answwer is #{answer}"
	puts "and your remainder is #{remainder}"
elsif operation == "exponent"
	answer = number1 ** number2
	puts "your answwer is #{answer}"
else
	puts "we can't do that"
end