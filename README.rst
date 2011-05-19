DjangoCms WrappedText plugin
============================

Description
-----------

Provide an extended text plugin allowing to wrap your entry into a css styled div.
Extends the classic text plugin and add simply a css input to configure your wrapper.

Prelude
-------

Install django and djangocms

Installation
------------

Download its tar.gz file (download link)::

    wget https://github.com/tonthon/cmsplugin_wrappedtext

Build::

    cd cmsplugin_wrappedtext
    sudo make install

Configuration

Add cmsplugin_wrappertext to your plugin entry in the settings.py file
Launch the syncdb command from inside your project::

    python manage.py syncdb
