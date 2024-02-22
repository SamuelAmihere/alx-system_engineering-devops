# Enable holberton to login and open files without any error.

# Increase the ULIMIT: Hard
exec { 'increase-hard-file-limit-for-holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  # specifying path for the sed command to exceute
  path    => '/usr/local/bin/:/bin/'
}

# Increase the ULIMIT: Soft
exec { 'increase-soft-file-limit-for-holberton':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  # specifying path for the sed command to exceute
  path    => '/usr/local/bin/:/bin/'
}
