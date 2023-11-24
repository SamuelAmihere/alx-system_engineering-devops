# Creating a file

file { '/tmp/school':
  mode    => '0744',
  owneer  => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
