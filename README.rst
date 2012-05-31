
Description
===========

This library provides helper classes for writing plugins for the server
monitoring tool Munin. It also comes with some prebuilt plugins for
various services including PostgreSQL, Memcached, and Nginx.


Tomcat plugin
-------------
Tomcat plugin works for Apache Tomcat, JBoss and Red5.

For Red5, you should create a new app into webapps named "status" with a file "status.jsp".

::
  <?xml version="1.0" encoding="utf-8"?>
  <%@ page language="java" pageEncoding="utf-8" contentType="text/xml" %>
  <status>
  	  <jvm>
 		  <memory free='<%= Runtime.getRuntime().freeMemory() %>' total='<%= Runtime.getRuntime().totalMemory() %>' max='<%= Runtime.getRuntime().maxMemory() %>'/>
	  </jvm>
  </status>

Create a empty WEB-INF directory into status app.