import { Flex, Grid, Spinner, Text } from "@chakra-ui/react";
import { USERS } from "../dummy/dummy";
import UserCard from "./UserCard";

const UserGrid = () => {
  return (
    <>
      <Grid
        templateColumns={{
          base: "1fr",
          md: "repeat(2, 1fr)",
          lg: "repeat(3, 1fr)",
        }}
        gap={4}
      >
        {USERS.map((user) => (
          <UserCard key={user.id} user={user} />
        ))}
      </Grid>
      (
      <Flex justifyContent={"center"}>
        <Spinner size={"xl"} />
      </Flex>
      ) (
      <Flex justifyContent={"center"}>
        <Text fontSize={"xl"}>
          <Text as={"span"} fontSize={"2xl"} fontWeight={"bold"} mr={2}>
            Poor you! 🥺
          </Text>
          No friends found.
        </Text>
      </Flex>
      )
    </>
  );
};
export default UserGrid;
