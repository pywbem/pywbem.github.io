/*
 * JavaScript support for CMPI pages project.
 *
 * Prerequisites:
 *  jquery.js V1.x from http://jquery.com/
 */

/*
 * This function loads a HTML file and adds its top element as a child node of
 * a target node, identified by its ID.
 *
 * Parameters:
 *   @param url (string): URL of the HTML file to be loaded.
 *   @param id (string): ID of the target element.
 */
function load_url_into_id(url, id)
{
  $('#' + id).load(url);
}
