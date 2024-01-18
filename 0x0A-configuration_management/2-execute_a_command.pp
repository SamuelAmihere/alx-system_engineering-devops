# Executing a command to kills killmenow

exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
