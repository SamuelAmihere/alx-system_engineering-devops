# Creating a file

file { '/tmp/school':
  content => 'I love Puppet',
  mode    => '0744',
  owneer  => 'www-data',
  group   => 'www-data',
}
