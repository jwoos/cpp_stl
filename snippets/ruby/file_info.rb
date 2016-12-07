file_name = gets.chomp
puts "file was #{file_name}"
infoName = File.path(file_name)

birthtime = infoName.birthtime
puts "Time created: #{birthtime}"

modtime = infoName.mtime
puts "Time edited: #{modtime}"

executable = infoName.executable?
puts "Executable? #{executable}"

owned = infoName.owned?
puts "Owned by user? #{owned}"

readable = infoName.readable?
puts "Readable by user? #{readable}"

writable = infoName.writable?
puts "Writable by user? #{writable}"

size = infoName.size(file_name)
puts "Size: #{size}"

worldreadable = infoName.world_readable?
puts "Readable by others? #{worldreadable}"

worldwritable = infoName.world_writable?
puts "Writable by others? #{worldwritable}"
