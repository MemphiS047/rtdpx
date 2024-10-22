// For temporarly 3 different sensor will be handled in this layer
// these temperature, pressure and accelerometer, later on depending
// on the flow of the development more and more abstractions and implementations
// for different sensors could be implemented (i.e. synthetic data generation)
class Sensor {
public:
  virtual double generateData();
  virtual 
}
