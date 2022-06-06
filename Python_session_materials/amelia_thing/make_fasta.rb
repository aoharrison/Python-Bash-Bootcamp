n = 1000

length = (100..10_000).to_a
letters = %w[A C T G]

n.times do |i|
  len = length.sample
  seq = len.times.map { |_| letters.sample }.join

  puts ">seq_#{i}\n#{seq}"
end
