class Car
    attr_reader :make, :model, :color, :price
  
    def initialize(make, model, color, price)
      @make = make
      @model = model
      @color = color
      @price = price
    end
  
    def set_price(p)
      @price = p
    end
  
    def paint(c)
      @color = c
    end
  
    def show_car_info
      puts "Make: #{@make}"
      puts "Model: #{@model}"
      puts "Color: #{@color}"
      puts "Price: $#{@price}"
    end
  end
  