import {
  Box,
  Button,
  Container,
  Flex,
  Text,
  useColorMode,
  useColorModeValue,
} from "@chakra-ui/react";
import { ImSun } from "react-icons/im";
import { TbMoonStars } from "react-icons/tb";
import CreateUserModal from "./CreateUserModel";

const Navbar = () => {
  const { colorMode, toggleColorMode } = useColorMode();
  return (
    <Container maxW={"900px"}>
      <Box
        px={4}
        my={4}
        borderRadius={5}
        bg={useColorModeValue("blue.200", "blue.700")}
        position="relative" // Position relative to use absolute positioning for the button
      >
        <Flex h="16" alignItems="center" justifyContent="center">
          <Text fontSize="lg" fontWeight={500} display={{ md: "block" }}>
            Name Cards
          </Text>
        </Flex>
        <Button
          onClick={toggleColorMode}
          position="absolute" // Position the button absolutely
          top="0"
          right="0"
          mt={2}
          mr={2}
        >
          {colorMode === "light" ? <TbMoonStars /> : <ImSun />}
        </Button>
        <CreateUserModal />
      </Box>
    </Container>
  );
};
export default Navbar;
