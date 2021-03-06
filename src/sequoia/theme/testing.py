# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import sequoia.theme


class SequoiaThemeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=sequoia.theme)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'sequoia.theme:default')


SEQUOIA_THEME_FIXTURE = SequoiaThemeLayer()


SEQUOIA_THEME_INTEGRATION_TESTING = IntegrationTesting(
    bases=(SEQUOIA_THEME_FIXTURE,),
    name='SequoiaThemeLayer:IntegrationTesting'
)


SEQUOIA_THEME_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SEQUOIA_THEME_FIXTURE,),
    name='SequoiaThemeLayer:FunctionalTesting'
)


SEQUOIA_THEME_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        SEQUOIA_THEME_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='SequoiaThemeLayer:AcceptanceTesting'
)
