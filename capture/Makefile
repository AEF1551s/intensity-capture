CC = g++
SDK_PATH = ./sdk
SRC_PATH = ./src
INCLUDE_PATH = ./include
BUILD_PATH = ./build
CFLAGS = -Wno-multichar -I $(SDK_PATH) -I $(INCLUDE_PATH) -fno-rtti -O3
LDFLAGS = -lm -ldl -lpthread

# Object files in build directory
OBJS = $(BUILD_PATH)/Capture.o $(BUILD_PATH)/Config.o $(BUILD_PATH)/DeckLinkAPIDispatch.o

# Target executable
TARGET = Capture

# Build target
$(TARGET): $(OBJS)
	$(CC) -o $(TARGET) $(OBJS) $(CFLAGS) $(LDFLAGS)

# Compile source files in src/
$(BUILD_PATH)/%.o: $(SRC_PATH)/%.cpp $(INCLUDE_PATH)/%.h | $(BUILD_PATH)
	$(CC) -c $< -o $@ $(CFLAGS)

# Compile DeckLinkAPIDispatch in sdk/
$(BUILD_PATH)/%.o: $(SDK_PATH)/%.cpp | $(BUILD_PATH)
	$(CC) -c $< -o $@ $(CFLAGS)

# Ensure build directory exists
$(BUILD_PATH):
	mkdir -p $(BUILD_PATH)

clean:
	rm -rf $(BUILD_PATH) $(TARGET)
