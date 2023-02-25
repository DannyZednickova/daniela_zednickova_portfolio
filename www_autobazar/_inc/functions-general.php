<?php
/**
 * 12 * Functions take care of system
 * 404
 * nice url links based on segments in url base_url/segment(1)/segment(2)
 * print r / var dump function for development
 *
 */


/**
 * Show 404
 *
 * Sends 404 not found header
 * And shows 404 HTML page
 *
 * @return void
 */
function show_404()
{
    http_response_code(404);
    include('404.php'); // provide your own HTML for the error page
    die();
}


/**
 * Asset
 *
 * Creates absolute URL to asset file
 *
 * @param string $path path to asset file
 * @param string $base asset base url
 * //trim '/' trims / from the begining of the string
 * // FILTER SANITAZE URL - MAKES SURE THERE IS JUST PURE LOOKING URL!
 * @return string   absolute URL to asset file
 */
function asset($path, $base = BASE_URL . '/assets/')
{
    $path = trim($path, '/');
    return filter_var($base . $path, FILTER_SANITIZE_URL);
}


/**
 * i need to get current URL, but i am not sure, if its httpS or http. So i check via ternar operator if in $_server is only http, or there is HTTPS switched on...
 * then i just "join" the rest of my url adress - http_host = localhost on my computer and request_uri will find excatly what is writen in URL such a /autobazar/delete/2 etc
 * then i use str_replace function to cut "BASE_URL" from it, parse_url then just make sure it takes only real PATH not oher else from URL.. .and i trim it from both sides from any "/". After i use explode function to get all the segments comming after my BASE_URL /hello/there/2 = it makes it an array...
 *
 */

function get_segments()
{
    $current_url = 'http' . (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] == 'on ' ? 's://' : '://') . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
    $path = str_replace(BASE_URL, '', $current_url);
    $path = trim(parse_url($path, PHP_URL_PATH), '/');
    $segments = explode('/', $path);
    return $segments;
}


/**
 *This returns the $index-th URI segment = i have URL www.dd.cz/hello/balls  i will write segment(1) and it will go through to a query string and gets me just "hello" etc :)
 *the INDEX-1 is there because in array we start [0] => segment... its PHP think...
 *
 */

function segment($index)
{
    $segments = get_segments();
    return isset($segments[$index - 1]) ? $segments[$index - 1] : false;
}


/**
 *  VAR DUMP AND PRINT R FUNCTION - do not need to writ it again for good sake...
 * NEED TO DELETE IT LATER"
 *
 */

function dannyprint($attr)
{
    echo '<pre>';
    print_r($attr);
    echo '</pre> ';
}