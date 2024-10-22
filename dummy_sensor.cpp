// Base sensor class 
class Sensor {
public:
  Sensor();
  Sensor(Sensor &&) = default;
  Sensor(const Sensor &) = default;
  Sensor &operator=(Sensor &&) = default;
  Sensor &operator=(const Sensor &) = default;
  ~Sensor();

private:
  
};

Sensor::Sensor() {
  
}

Sensor::~Sensor() {
}
