# Strace is my friend for fixing sever: Fixing bad `phpp` extensions to `php`

$src_file = '/var/www/html/wp-settings.php'

exec { 'fix-wordpress':
  command => "sed -i s/phpp/php/g ${src_file}",
  path    => '/usr/local/bin/:/bin/'
}
