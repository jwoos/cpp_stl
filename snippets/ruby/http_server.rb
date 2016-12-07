require 'webrick'

root = File.expand_path Dir.pwd
server = WEBrick::HTTPServer.new :Port =>2000, :DocumentRoot => root

trap 'INT' do server.shutdown end

server.start
