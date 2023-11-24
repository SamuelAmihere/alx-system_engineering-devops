# Executing a command to kills killmenow

exe {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
