require 'car' 

describe Car do
  subject { Car.new("Toyota", "Camry", "Red", 25000) }

  describe "#initialize" do
    it "sets the make, model, color, and price attributes" do
      expect(subject.make).to eq "Toyota"
      expect(subject.model).to eq "Camry"
      expect(subject.color).to eq "Red"
      expect(subject.price).to eq 25000
    end
  end

  describe "#set_price" do
    it "updates the price attribute" do
      subject.set_price(30000)
      expect(subject.price).to eq 30000
    end
  end

  describe "#paint" do
    it "updates the color attribute" do
      subject.paint("Blue")
      expect(subject.color).to eq "Blue"
    end
  end

  describe "#show_car_info" do
    it "prints the car information in the expected format" do
      expected_output = <<~OUTPUT
        Make: Toyota
        Model: Camry
        Color: Red
        Price: $25000
      OUTPUT

      expect { subject.show_car_info }.to output(expected_output).to_stdout
    end
  end
end
