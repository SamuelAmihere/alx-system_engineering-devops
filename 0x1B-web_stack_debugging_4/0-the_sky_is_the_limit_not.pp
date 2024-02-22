# Increasing the traffic amount an Nginx server.

# Increase the ULIMIT
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  # specifying path for the sed command to exceute
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  # specifying path for the init.d file
  path    => '/etc/init.d/'
}
