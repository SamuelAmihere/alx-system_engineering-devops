# Installing a package

file {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
