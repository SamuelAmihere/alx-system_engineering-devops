#!/usr/bin/pup
# Install a package

file { 'flask':
  provider => 'pip3',
  ensure   => '2.1.0',
}
