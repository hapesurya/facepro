from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu


class SlidingDoorsMenu(CMSAttachMenu):
    name = _("SlidingDoorsMenu")

    def get_nodes(self, request):
        nodes = []
        node1 = NavigationNode(
            title=_('Sliding Door SL3'),
            url="/products/sliding-doors/sl3/",
            id=1,
            )
        node2 = NavigationNode(
            title=_('Sliding Door SL4'),
            url="/products/sliding-doors/sl4/",
            id=2,
            )
        node3 = NavigationNode(
            title=_('Sliding Door SL5'),
            url= "/products/sliding-doors/sl5/",
            id= 3,
            )
        node4 = NavigationNode(
            title=_('Sliding Door SL6'),
            url="/products/sliding-doors/sl6/",
            id=4,
            )
        nodes.append(node1)
        nodes.append(node2)
        nodes.append(node3)
        nodes.append(node4)
        return nodes

menu_pool.register_menu(SlidingDoorsMenu)