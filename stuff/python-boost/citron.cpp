#include <iostream>
 
using namespace std;
  
void say_hello(const char* name) {
      cout << "Hello " <<  name << "!\n";}
       
void init()
{
}

#include <boost/python/module.hpp>
#include <boost/python/def.hpp>

using namespace boost::python;
        
BOOST_PYTHON_MODULE(citron)
{
            def("say_hello", say_hello);
}