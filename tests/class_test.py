from loguru import logger


class TestClass(object):
    x = 1
    y = 2

    def test_class_method_x(self):
        logger.debug("Running TestClass.test_class_method")
        assert self.x != 2

    def test_class_method_y(self):
        logger.debug("Running TestClass.test_primitive")
        assert self.y == 2
