var http = require('http');

var routes = {
  "get/.*" : function(request, response) {
    var resp = "get/*";
    response.writeHead(200, {
      "Content-Type": "text/plain",
      "Content-Length": resp.length});
    response.end(resp);
  },
  "put/[ab]*/plop/(a|b)c$" : function(request, response) {
    var resp = "put/*";
    response.writeHead(200, {
      "Content-Type": "text/plain",
      "Content-Length": resp.length});
    response.end(resp);
  },
  ".*" : function(request, response) {
    var resp = "Default";
    response.writeHead(200, {
      "Content-Type": "text/plain",
      "Content-Length": resp.length});
    response.end(resp);
  }
};

function Router(routes) {
  this.routes = routes;
  this.cached_routes = {};
}

Router.prototype.route = function(request, response) {
  for (var route in this.routes) {
    var re = this.cached_routes[route];
    if (re === undefined) {
      re = this.cached_routes[route] = new RegExp(route);
    }
    if (re.test(request.url)) {
      routes[route](request, response);
    }
  }
};

var router = new Router(routes);

http.createServer(function (request, response) {
  router.route(request, response);
}).listen(8125);
