# Creating a file

file { 'school':
  mode    => '0744',
  owneer  => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
  path    => '/tmp/school',
}
